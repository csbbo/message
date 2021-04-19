import logging

import bson
import pymongo

from message.validate import *
from utils.filters import objectid_validator
from utils.http import APIView, check, get_login_user, jsondumps
from utils.shortcuts import utcnow

logger = logging.getLogger(__name__)


class MessageAPI(APIView):
    @check(validate=message_post_validator)
    async def post(self):
        data = self.request_data
        try:
            insert_result = await self.db.messages.insert_one({
                'uid': self.request_user['_id'],
                'title': data['title'],
                'content': data['content'],
                'ip': self.request.remote,
                'user-agent': self.request.headers.get('user-agent'),
            })
        except pymongo.errors.DuplicateKeyError:
            return self.error(self.i18n.message_not_exists)
        except Exception as e:
            logger.exception(e)
            return self.error(self.i18n.server_error)

        return self.success({'id': str(insert_result.inserted_id)})

    async def get(self):
        try:
            message_id = bson.ObjectId(self.request.rel_url.query.get('id'))
        except bson.errors.InvalidId:
            return self.error(self.i18n.message_not_exists)

        message = await self.db.messages.find_one({'_id': message_id})
        if not message:
            return self.error(self.i18n.message_not_exists)
        return self.success({'message': message})

    @check(validate=objectid_validator)
    async def delete(self):
        data = self.request_data
        update_result = await self.db.messages.update_one(
            {
                '_id': bson.ObjectId(data['id']),
                'uid': self.request_user['_id']
            },
            {
                '$set': {
                    'delete_time': utcnow()
                }
            }
        )
        if not update_result.modified_count:
            return self.error(self.i18n.message_not_exists)
        return self.success()


class MessageListAPI(APIView):
    async def get(self):
        flt = {'delete_time': None}
        if content := self.request.rel_url.query.get('content'):
            flt['content'] = {'$regex': content}

        messages_list = []
        async for m in self.db.messages.find(flt):
            messages_list.append({
                'id': str(m['_id']),
                'title': m['title'],
                'content': m['content']
            })
        return self.success({'messages': messages_list})


class CommentAPI(APIView):
    @check(validate=comment_post_validator)
    async def post(self):
        data = self.request_data
        message = await self.db.messages.find_one({'_id': bson.ObjectId(data['mid'])})
        if not message:
            return self.error(self.i18n.message_not_exists)

        user = await get_login_user(self.request)
        data['uid'] = user['_id'] if user else None

        try:
            insert_result = await self.db.comments.insert_one({
                'uid': data['uid'],
                'mid': message['_id'],
                'content': data['content'],
                'ip': self.request.remote,
                'user-agent': self.request.headers.get('user-agent'),
            })
        except Exception as e:
            logger.exception(e)
            return self.error(self.i18n.server_error)
        await self.sio.emit('room1', jsondumps({'comment': data['content']}))
        return self.success({'id': str(insert_result.inserted_id)})

    async def get(self):
        try:
            comment_id = bson.ObjectId(self.request.rel_url.query.get('id'))
        except bson.errors.InvalidId:
            return self.error(self.i18n.comment_not_exists)

        comment = await self.db.comments.find_one({'_id': comment_id})
        if not comment:
            return self.error(self.i18n.comment_not_exists)
        return self.success({'comment': comment})


class CommentListAPI(APIView):
    @check(login_required=False, validate=comment_list_get_validator)
    async def get(self):
        flt = {'delete_time': None}

        if mid := self.request.rel_url.query.get('mid'):
            flt.update({'mid': bson.ObjectId(mid)})

        if content := self.request.rel_url.query.get('content'):
            flt['content'] = {'$regex': content}

        comment_list = []
        async for m in self.db.comments.find(flt):
            comment_list.append({
                'id': str(m['_id']),
                'content': m['content']
            })
        return self.success({'comments': comment_list})
