<template>
  <div class="container" style="background-color:#bfbfbf"><br><br>
    <p class="text-muted">Games Department</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <p style="color:red;">{{message}}</p>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="gameitem.id" v-for="gameitem in Gamesitems">
        <td>
          {{gameitem.item_name}}
        </td>
        <td>
          {{gameitem.cash_value}}
        </td>
      </tr>
    </table>
    <br>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000/'
import axios from 'axios'
export default {
  name: 'Games',
  data () {
    return {
      Gamesitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: ''
    }
  },
  mounted () {
    this.getGamesItems()
  },
  methods: {
    getGamesItems() {
      axios({
        method: 'get',
        url: API_URL + 'gamesdepartment/',
        auth: {
          username: 'freddy',
          password: 'voldermort'
        }
      }).then(response => this.Gamesitems = response.data)
    },
    checkDatabase() {
      if (this.Gamesitems == '' ) {
        this.message = 'You have been successfully cleared from this department';
      }
      else {
        this.message = 'Please check with the department and clear your record before proceeding.'
        this.showTable =  true;
      }
    }
  }
}
</script>

<style scoped>

</style>
