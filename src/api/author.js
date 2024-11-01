import request from '@/utils/request'

// 添加作者信息
export function createAuthorInfo(data){
    return request({
        url: "/author/",
        method: 'post',
        data
    })
}

// 获取所有者信息
export function getAuthorInfo() {
    return request({
        url: "/author/",
        method: 'get',
    })
}

//通过作者ID获取作者信息
export function getAuthorInfoById(id) {
    return request({
        url: "/author/" + id,
        method: 'get',
    })
}

//更新作者信息(待完善)
export function UpdateAuthorInfoById(id) {
    return request({
        url: "/author/" + id,
        method: 'put',
    })
}

// 删除作者信息接口
export function DeleteAuthorInfoById(id) {
    return request({
        url: "/author/" + id,
        method: 'delete',
    })
}