import request from '@/utils/request'

// 搜索URL
export function get_system_info() {
  return request({
    url: '/system_info/',
    method: 'get'
  })
}

export function get_lan_info() {
  return request({
    url: '/system_info/get_lan_info',
    method: 'get'
  })
}

export function get_db_info() {
  return request({
    url: '/databases/get_db_info',
    method: 'get'
  })
}

export function switch_db(data) {
  return request({
    url: '/databases/switch_db',
    method: 'post',
    data
  })
}

export function get_db_tables(data) {
  return request({
    url: '/databases/get_db_tables',
    method: 'post',
    data
  })
}

export function get_databases() {
  return request({
    url: '/databases/get_databases',
    method: 'get'
  })
}

export function update_project() {
  return request({
    url: '/system_info/update_project',
    method: 'get'
  })
}

export function compile_project() {
  return request({
    url: '/system_info/compile_project',
    method: 'get'
  })
}

export function restart_project() {
  return request({
    url: '/system_info/restart_project',
    method: 'get'
  })
}

export function one_click_restart() {
  return request({
    url: '/system_info/one_click_restart',
    method: 'get'
  })
}
