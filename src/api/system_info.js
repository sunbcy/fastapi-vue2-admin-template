import request from '@/utils/request'

// 搜索URL
export async function get_system_info() {
  return await request({
    url: '/system_info/',
    method: 'get'
  })
}

export async function get_lan_info() {
  return await request({
    url: '/system_info/get_lan_info',
    method: 'get'
  })
}

export async function get_db_info() {
  return await request({
    url: '/databases/get_db_info',
    method: 'get'
  })
}

export async function switch_db(data) {
  return await request({
    url: '/databases/switch_db',
    method: 'post',
    data
  })
}

export async function get_db_tables(data) {
  return await request({
    url: '/databases/get_db_tables',
    method: 'post',
    data
  })
}

export async function get_databases() {
  return await request({
    url: '/databases/get_databases',
    method: 'get'
  })
}

export async function update_project() {
  return await request({
    url: '/system_info/update_project',
    method: 'get'
  })
}

export async function compile_project() {
  return await request({
    url: '/system_info/compile_project',
    method: 'get'
  })
}

export async function restart_project() {
  return await request({
    url: '/system_info/restart_project',
    method: 'get'
  })
}

export async function one_click_restart() {
  return await request({
    url: '/system_info/one_click_restart',
    method: 'get'
  })
}
