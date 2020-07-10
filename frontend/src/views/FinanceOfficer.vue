<template>
  <div class="container" style="background-color:#43fad5">
    <br><br>
    <p class="text-muted">Finance Officer</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <p style="color:red;">{{message}}</p>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="finoffitem.id" v-for="finoffitem in FinanceOfficeritems">
        <td>
          {{finoffitem.item_name}}
        </td>
        <td>
          {{finoffitem.cash_value}}
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
  name: 'FinanceOfficer',
  data () {
    return {
      FinanceOfficeritems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: ''
    }
  },
  mounted () {
    this.getFinanceOfficerItems()
  },
  methods: {
    getFinanceOfficerItems() {
      axios({
        method: 'get',
        url: API_URL + 'financeofficer/',
        auth: {
          username: 'freddy',
          password: 'voldermort'
        }
      }).then(response => this.FinanceOfficeritems = response.data)
    },
    checkDatabase() {
      if (this.FinanceOfficeritems == '' ) {
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
