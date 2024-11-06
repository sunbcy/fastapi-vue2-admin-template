<template>
  <div>
    <!-- 显示在线设备数量 -->
    <div class="online-count">
      数据库监测数量: {{ DatabasesCount }}
    </div>
    <el-table :data="tableData" style="width: 100%; height: 284px; max-height: 284px; overflow-y: auto;">
      <el-table-column prop="dbName" label="DB_NM" width="130">
        <template slot-scope="scope">
          <span v-if="scope.row.status === 'ON'" @click="fetchDatabases(scope.row)">{{ scope.row.dbName }}</span>
          <span v-else>{{ scope.row.dbName }}</span>
        </template>
        <!--        <template slot-scope="scope">-->
        <!--          <span @click="fetchTables(scope.row)" v-if="scope.row.status === 'ON'">{{ scope.row.dbName }}</span>-->
        <!--          <span v-else>{{ scope.row.dbName }}</span>-->
        <!--        </template>-->
      </el-table-column>
      <el-table-column prop="status" label="DB_STATUS" width="130">
        <template slot-scope="scope">
          <span v-if="scope.row.status === 'ON'">✅</span>
          <span v-else>❌</span>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="DB_SWITCH" width="130">
        <template slot-scope="scope">
          <el-switch
            v-model="scope.row.status"
            active-value="ON"
            inactive-value="OFF"
            @change="handleSwitchChange(scope.row)"
          />
        </template>
      </el-table-column>
      <!--el-table-column prop="port" label="PORT" width="130"></el-table-column-->
    </el-table>

    <el-dialog :visible.sync="dialogVisible" title="Databases" width="80%">
      <el-tabs v-model="activeTab" type="card" @tab-click="handleTabClick">
        <el-tab-pane v-for="(database, index) in databasesList" :key="index" :label="database.name" :name="database.name">
          <el-table v-if="database.tables && database.tables.length > 0" :data="database.tables" style="width: 100%">
            <el-table-column prop="name" label="Table Name" width="200px" />
          </el-table>
          <p v-else>Loading tables...</p>
        </el-tab-pane>
      </el-tabs>
    </el-dialog>

    <!--    <el-dialog :visible.sync="dialogVisible" title="Databases">-->
    <!--      <el-table :data="databasesList" style="width: 100%">-->
    <!--        <el-table-column prop="name" label="Database Name" width="200px"></el-table-column>-->
    <!--      </el-table>-->
    <!--    </el-dialog>-->

    <!--    <el-dialog :visible.sync="dialogVisible" title="Data Tables">-->
    <!--      <el-table :data="tables" style="width: 100%">-->
    <!--        <el-table-column prop="tableName" label="Table Name" width="200px"></el-table-column>-->
    <!--      </el-table>-->
    <!--    </el-dialog>-->
  </div>
</template>

<script>
import { get_db_info } from '@/api/system_info'
import { get_db_tables } from '@/api/system_info'
import { get_databases } from '@/api/system_info'
import { switch_db } from '@/api/system_info'

export default {
  name: 'DatabasesTable',
  data() {
    return {
      tableData: [],
      dialogVisible: false,
      tables: [],
      databasesList: [],
      activeTab: ''
    }
  },
  computed: {
    DatabasesCount() {
      return this.tableData.length
    }
  },
  mounted() {
    // 组件挂载时立即运行一次
    this.get_db_info_interval()

    // 每隔半分钟再运行一次
    this.intervalId = setInterval(() => { this.get_db_info_interval() }, 30 * 1000) // 每隔1min切换一次状态
  },
  beforeDestroy() {
    // 清除定时器，防止内存泄漏
    if (this.intervalId) {
      clearInterval(this.intervalId)
    }
  },
  methods: {
    get_db_info_interval() {
      get_db_info().then(res => {
        // console.log(res.searchResults)
        this.tableData = res.searchResults
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 获取LAN host失败!')
      })
    },
    handleSwitchChange(row) {
      // 在这里处理切换事件，例如更新后端数据
      console.log(`Switch changed for ${row.dbName}: ${row.status}`)
      // 你可以在这里添加代码来将状态更新到后端
      const req_Data = {
        'dbName': row.dbName,
        'status': row.status
      }
      switch_db(req_Data)
        .then(res => {
          // this.searchResults = res.searchResults
          console.log(res.searchResults)
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常, 职位搜索失败.')
        })
    },
    async fetchDatabases(row) {
      if (row.status === 'ON') {
        get_databases().then(res => {
          console.log(res.searchResults)
          this.databasesList = res.searchResults.map(db => ({ name: db, tables: [] }))
          console.log(this.databasesList)
          this.dialogVisible = true
          this.activeTab = this.databasesList[0].name // 默认选中第一个数据库
          this.fetchTables(this.activeTab) // 获取第一个数据库的表
        }).catch(err => {
          console.log(err)
          this.$message.error('服务端异常, 获取 databases 失败!')
        })
      }
    },
    async fetchTables(databaseName) {
      const reqData = {
        'req': databaseName
      }
      get_db_tables(reqData).then(res => {
        console.log(res.searchResults)
        // this.tables = res.searchResults;
        // this.dialogVisible = true;
        const tables = res.searchResults
        const database = this.databasesList.find(db => db.name === databaseName)
        if (database) {
          database.tables = tables.map(table => ({ name: table }))
        }
      }).catch(err => {
        console.log(err)
        this.$message.error('服务端异常, 获取 tables 失败!')
      })
    },
    handleTabClick(tab) {
      this.fetchTables(tab.paneName) // 切换标签页时获取对应数据库的表
    }

  }
}
</script>

<style scoped>
/* 你可以在这里添加样式 */
.online-count {
  margin-top: 0px;
  font-size: 16px;
  color: #333;
}
</style>
