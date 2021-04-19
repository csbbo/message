import axios from 'axios'
import qs from 'qs'

const fetchData = (url = '', data = {}, method = 'GET') => {
    if (method === 'GET') {
        let param = qs.stringify(data)
        return new Promise(resolve => {
            axios.get(url+'?'+param).then((resp) => {
                resolve(resp.data)
            })
        })

    } else {
        return new Promise(resolve => {
            axios({
                method: method,
                url: url,
                data: data
            }).then((resp) => {
                resolve(resp.data)
            });
        })

    }
}


export const LoginAPI = data => fetchData('/api/LoginAPI', data, 'POST')
export const LogoutAPI = data => fetchData('/api/LogoutAPI', data, 'POST')
export const RegisterAPI = data => fetchData('/api/RegisterAPI', data, 'POST')
export const GetUser = () => fetchData('/api/UserAPI', {}, 'GET')

export const AddMessage = data => fetchData('/api/MessageAPI', data, 'POST')
export const GetMessage = data => fetchData('/api/MessageAPI', data, 'GET')
export const QueryMessage = data => fetchData('/api/MessageListAPI', data, 'GET')
export const DeleteMessage = data => fetchData('/api/MessageAPI', data, 'DELETE')
export const AddComment = data => fetchData('/api/CommentAPI', data, 'POST')
export const GetComment = data => fetchData('/api/CommentAPI', data, 'GET')
export const QueryComment = data => fetchData('/api/CommentListAPI', data, 'GET')
