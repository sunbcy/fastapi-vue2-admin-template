import request from '@/utils/request'

// export function login(data) {
//   return request({
//     url: '/users/login', //  /vue-admin-template Flask后端登陆接口
//     method: 'post', //请求方法
//     data //请求参数,这里是用户名和密码
//   })
// }

export function login(data) {
  return request({
    url: '/vue-admin-template/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/vue-admin-template/user/info', // /vue-admin-template
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout', // /vue-admin-template
    method: 'post'
  })
}
