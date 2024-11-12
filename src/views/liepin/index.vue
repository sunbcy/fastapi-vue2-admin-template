<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 24 }" :lg="{ span: 24 }" :xl="{ span: 24 }">
        <!-- 上半部分内容 -->
        <div>
          <h2>查询</h2>
          <div>
            <el-input v-model="searchJobKeyword" type="text" placeholder="输入职位" class="custom-input" @keyup.enter.native="search" />
            <el-button type="primary" @click="search">搜索</el-button>
          </div>

          <div>
            <label for="region">选择地区：</label>
            <el-select id="region" v-model="selectedRegion">
              <el-option value="410">全国</el-option>
              <el-option v-for="(region, code) in regions" :key="region" :value="region">{{ code }}</el-option>
            </el-select>
          </div>

        </div>
      </el-col>

      <el-col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 12 }" :lg="{ span: 12 }" :xl="{ span: 12 }">
        <!-- 下面-左侧或上半部分内容 -->
        <div class="grid-content bg-purple blur-background">
          <h2>数据库概览</h2>
          <p>职位总数: {{ jobNum }}</p>
          <p>公司总数: {{ compNum }}</p>

        </div>
      </el-col>
      <el-col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 12 }" :lg="{ span: 12 }" :xl="{ span: 12 }">
        <!-- 下面-右侧或下半部分内容 -->
        <div ref="contentContainer" class="grid-content bg-purple-light  blur-background long-cnt" @scroll="handleScroll">
          <h2>筛选</h2>
          <div>
            <el-button type="primary" @click="exportData">导出为 JSON</el-button>
          </div>

          <div>
            <div class="search-results">
              <div
                v-for="result in searchResults"
                :key="result.id"
                class="card"
                @click="fetchDetails(result.job_link)"
              >
                <div>
                  <h3>【{{ result.id }}】 {{ result.job_title }} {{ result.job_dq }}</h3>
                  <span class="job-salary">{{ result.job_salary }}</span>
                </div>
                <div>
                  <span class="label-tag">{{ result.job_requireWorkYears }}</span>
                  <span class="label-tag">{{ result.job_requireEduLevel }}</span>
                  <span class="label-tag">{{ result.job_labels }}</span>
                </div>
                <div>
                  <a :href="result.comp_link" class="company-info link-style" target="_blank"> {{ result.compName }}</a>
                  <span class="company-info"> {{ result.compIndustry }}</span>
                  <span class="company-info"> {{ result.compScale }}</span>
                </div>
                <a :href="result.job_link" class="link-style" target="_blank">{{ result.job_link }}</a>
              </div>
            </div>
          </div>

          <!-- 回到顶部按钮 -->
          <div v-show="showBackToTopButton" class="back-to-top-container" @click="scrollToTop">
            <el-tooltip placement="top" content="回到顶部">
              <i class="el-icon-arrow-up" />
            </el-tooltip>
          </div>
        </div>

      </el-col>
    </el-row>

    <!--      <el-tooltip placement="top" content="ToTop">-->
    <!--        <back-to-top :custom-style="myBackToTopStyle" :visibility-height="300" :back-position="50" transition-name="fade" />-->
    <!--      </el-tooltip>-->

    <!-- 对话框组件 -->
    <el-dialog :visible.sync="dialogVisible" title="职位详情" width="87%">
      <p v-if="details && details.job_tags">{{ details.job_tags }}</p>
      <p v-if="details && details.job_intro_content" v-html="formattedJobDetailIntro" />
      <p v-if="details && details.company_intro" v-html="formattedCompanyIntro" />
      <p v-if="details && details.company_info" v-html="formattedCompanyInfo" />
      <p v-else>加载中...</p>
    </el-dialog>

  </div>
</template>

<script>
import { search_jobs, get_job_num, get_comp_num, getJobDetails } from '@/api/liepin'
// import BackToTop from '@/components/BackToTop'
import { saveAs } from 'file-saver'
import Blob from 'blob'

export default {
  // components: { BackToTop },
  data() {
    return {
      details: null, // 用于存储从后端获取的详情
      dialogVisible: false, // 控制对话框显示的属性
      jobNum: '',
      compNum: '',
      searchJobKeyword: 'Python爬虫',
      searchResults: [],
      selectedRegion: '410', // 用于保存用户选择的地区代码
      regions: { // 地区选项列表，键为地区名称，值为地区代码
        '北京': '010',
        '上海': '020',
        '重庆': '040',
        '广州': '050020',
        '深圳': '050090',
        '成都': '280020',
        '杭州': '070020',
        '南京': '060020',
        '武汉': '170020',
        '苏州': '060080'
        // 可根据实际需求添加更多地区选项
      },
      // customizable button style, show/hide critical point, return position
      myBackToTopStyle: {
        right: '50px',
        bottom: '50px',
        width: '40px',
        height: '40px',
        'border-radius': '4px',
        'line-height': '45px', // 请保持与高度一致以垂直居中 Please keep consistent with height to center vertically
        background: '#e7eaf1' // 按钮的背景颜色 The background color of the button
      },
      dataToExport: {
        // 这里是你要导出的变量内容
        key: 'value'
      },
      showBackToTopButton: false
    }
  },
  computed: {
    // eslint-disable-next-line vue/return-in-computed-property
    formattedJobDetailIntro() {
      if (this.details && this.details.job_intro_content) {
        return this.details.job_intro_content.replace(/\n/g, '<br>')
      }
    },
    // eslint-disable-next-line vue/return-in-computed-property
    formattedCompanyIntro() {
      if (this.details && this.details.company_intro) {
        return this.details.company_intro.replace(/\n/g, '<br>')
      }
    },
    // eslint-disable-next-line vue/return-in-computed-property
    formattedCompanyInfo() {
      if (this.details && this.details.company_info) {
        return this.details.company_info.replace(/\n/g, '<br>')
      }
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    setTimeout(this.getJobNum(), 300)
    this.getCompNum()
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    fetchDetails(jobUrl) {
      const req_Data = {
        'city': this.selectedRegion,
        'dq': this.selectedRegion,
        'currentPage': 0,
        'key': this.searchJobKeyword,
        'workYearCode': '0'
      }
      const reqData = {
        'jobUrl': jobUrl,
        'payload': req_Data
      }
      this.dialogVisible = true
      getJobDetails(reqData).then(res => {
        this.details = res.searchResults
        console.log('Details:', this.details) // 调试信息
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 职位detail搜索失败')
      })
    },
    getJobNum() {
      get_job_num().then(res => {
        this.jobNum = res.searchResults
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 职位数目搜索失败')
      })
    },
    getCompNum() {
      get_comp_num().then(res => {
        this.compNum = res.searchResults
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 公司数目搜索失败')
      })
    },
    search() {
      // 这里可以编写发送请求获取搜索结果的逻辑, 例如使用Axios或者Fetch API
      console.log('search ' + this.searchJobKeyword)
      const req_Data = {
        'city': this.selectedRegion,
        'dq': this.selectedRegion,
        'currentPage': 0,
        'key': this.searchJobKeyword,
        'workYearCode': '0'
      }
      // const req_Data_json = JSON.stringify(req_Data)
      console.log(req_Data)
      search_jobs(req_Data)
        .then(res => {
          this.searchResults = res.searchResults
          this.dataToExport.key = res.searchResults
          // console.log(this.searchResults);
          setTimeout(() => {
            this.searchResults = res.searchResults
            this.dataToExport.key = res.searchResults
          }, 500)
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常, 职位搜索失败.')
        })

      // 示例中用settimeout模拟异步请求
    },
    exportData() {
      const jsonData = JSON.stringify(this.dataToExport, null, 2)
      const blob = new Blob([jsonData], { type: 'application/json' })
      // 文件名默认为搜索的职位名称加搜索时间
      const fileNamePrefix = this.searchJobKeyword
      // 创建一个新的 Date 对象以获取当前时间
      const now = new Date()

      // 定义一个函数来格式化日期
      function formatDate(date) {
        const year = date.getFullYear()
        const month = String(date.getMonth() + 1).padStart(2, '0') // 月份从0开始，需要+1
        const day = String(date.getDate()).padStart(2, '0')
        const hours = String(date.getHours()).padStart(2, '0')
        const minutes = String(date.getMinutes()).padStart(2, '0')
        const seconds = String(date.getSeconds()).padStart(2, '0')

        // 返回格式化的日期字符串，例如：2024-09-24T20-20-20
        return `${year}-${month}-${day}T${hours}-${minutes}-${seconds}`
      }

      // 获取格式化后的搜索时间
      const searchTime = formatDate(now)
      // 构建完整的文件名
      const fileName = `${fileNamePrefix}_${searchTime}.json`
      saveAs(blob, fileName)
    },
    handleScroll(event) {
      const scrollTop = event.target.scrollTop
      this.showBackToTopButton = scrollTop > 300
    },
    scrollToTop() {
      const container = this.$refs.contentContainer
      container.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }
  }
}
</script>

  <style lang="scss" scoped>
  .grid-content {
    display: flex;
    flex-direction: column;
    //align-items: center;
    //justify-content: center;
    color: white;
    font-size: 12px;
    padding: 20px;
  }

  .long-cnt {
    height: 100%; /* 使内容区域占满可用空间 */
    overflow-y: auto; /* 添加垂直滚动条 */
  }

  .bg-purple {
    background-color: #99a9bf;
  }

  .bg-purple-light {
    background-color: #d3dce6;
  }

  .blur-background {
    backdrop-filter: blur(10px); /* 高斯模糊效果 */
    -webkit-backdrop-filter: blur(10px); /* Safari 和 Chrome 兼容 */
  }

  /* 桌面端样式 */
  @media (min-width: 768px) {
    .grid-content {
      height: 100vh; /* 每个部分占据视口高度的一半 */
    }
  }

  /* 移动端样式 */
  @media (max-width: 767px) {
    .grid-content {
      height: 50vh; /* 每个部分占据视口高度的一半 */
    }
  }

  .dashboard {
    &-container {
      margin: 30px;
    }
    &-text {
      font-size: 30px;
      line-height: 46px;
    }
  }

  .custom {
    &-input {
      width:80%
    }
  }

  .search-results {
    display: flex;
    flex-direction: column; /*卡片竖向排列 */
    // align-items: center;
  }

  .card, .details-card {
    width: 80%;
    padding: 20px;
    margin: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow:0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
  }

  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .card a {
    display: inline-block;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;  // 防止url过长，显示异常
    white-space: nowrap;
}
  .job-salary {
    flex-shrink: 0;
    margin-left: 12px;
    font-size: 18px;
    line-height: 25px;
    font-weight: bold;
    color: rgb(255, 100, 0);
  }

  .label-tag {
    margin-right: 8px;
    font-size: 12px;
    line-height: 22px;
    border-radius: 6px;
    padding: 0 8px;
    color: rgb(102, 102, 102);
    background-color: rgb(248, 249, 251);
  }

  .company-info {
    flex-shrink: 0;
    max-width: 290px;
    padding-left: 8px;
    line-height: 17px;
    font-size: 12px;
    color: rgb(7, 19, 43);
  }

  h3 {
    margin: 0 0 10px;
  }

  p {
    margin: 0;
  }

  .link-style {
    text-decoration: none;
    color: #007bff;
    transition: color 0.3s, text-decoration 0.3s;
  }

  .link-style:hover {
    color: #0056b3;
    text-decoration: underline;
  }

  .back-to-top-container {
    position: fixed; /* 固定定位 */
    right: 20px; /* 距离右边 20px */
    bottom: 20px; /* 距离底部 20px */
    z-index: 1000; /* 确保按钮在其他元素之上 */
    cursor: pointer;
  }

  .back-to-top-container .el-tooltip__popper {
    background-color: #fff;
    border: 1px solid #ebeef5;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    color: #303133;
  }
  </style>
