import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),

      meta: { title: '首页', icon: 'dashboard' }
    }]
  },

  {
    path: '/big_a_stock',
    component: Layout,
    redirect: '/big_a_stock',
    name: 'BigAStock',
    meta: { title: 'A股市场分析', icon: 'IconParkOutlineStockMarket' },
    children: [
      {
        path: 'https://dapanyuntu.com/',
        meta: { title: '大盘云图', icon: 'EmojioneV1StockChart' }
      },
      {
        path: 'jiucaigongshe',
        name: 'Jiucaigongshe',
        component: () => import('@/views/jiucaigongshe/index'),
        meta: { title: '韭研公社', icon: 'jiucaigongshe' }
      }
    ]
  },

  {
    path: '/findjob',
    component: Layout,
    redirect: '/findjob/liepin',
    name: 'FindJobs',
    meta: { title: '找工作', icon: 'briefcase-solid' },
    children: [
      {
        path: 'liepin',
        name: 'Liepin',
        component: () => import('@/views/liepin/index'),
        meta: { title: '猎聘网', icon: 'liepin' }
      }
    ]
  },

  {
    path: '/entertainment',
    component: Layout,
    redirect: '/entertainment/netease_music',
    name: 'Entertainment',
    meta: { title: '娱乐', icon: 'StreamlineEntertainmentMusicNote1MusicAudioNote' },
    children: [
      {
        path: 'netease_music',
        name: 'Netease_music',
        component: () => import('@/views/netease_music/index'),
        meta: { title: '网易云音乐', icon: 'netease_music_macos_bigsur_icon_189918' }
      },
      {
        path: 'https://tool.liumingye.cn/music/#/',
        meta: { title: '刘明野的工具箱', icon: 'tool.liumingye.cn' }
      }
    ]
  },

  {
    path: '/analysis_tools',
    component: Layout,
    redirect: '/analysis_tools/pcap_analysis',
    name: 'AnalysisTools',
    meta: { title: '流量分析工具', icon: 'analysis' },
    children: [
      {
        path: 'pcap_analysis',
        name: 'PcapAnalysis',
        component: () => import('@/views/pcap_analysis/index'),
        meta: { title: '数据包分析', icon: 'network' }
      }
    ]
  },

  {
    path: '/send_info',
    component: Layout,
    redirect: '/send_info/qiyewechat',
    name: 'Sendinfo',
    meta: { title: '发通知', icon: 'message-solid' },
    children: [
      {
        path: 'qiyewechat',
        name: 'QiYeWechat',
        component: () => import('@/views/qiyewechat/index'),
        meta: { title: '企业微信', icon: 'qiyewechat' }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
