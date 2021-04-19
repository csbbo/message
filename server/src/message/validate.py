from utils import filters as f

message_post_validator = {
    'title': [f.required, f.not_empty],
    'content': [f.not_empty],
}

comment_post_validator = {
    'mid': [f.required, f.objectid],
    'content': [f.required, f.not_empty]
}

comment_list_get_validator = {
    'mid': [f.objectid],
    'content': [f.not_empty]
}