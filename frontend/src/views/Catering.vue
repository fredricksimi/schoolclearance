<template>
  <div class="container" style="background-color:rgb(255, 220, 123)">
    <br><br>
    <p class="text-muted">Catering Department</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <div :class="alert">{{message}}</div>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="catitem.id" v-for="catitem in cateringitems">
        <td>
          {{catitem.item_name}}
        </td>
        <td>
          {{catitem.cash_value}}  
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
  name: 'Catering',
  data () {
    return {
      cateringitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: '',
      alert:''
    }
  },
  mounted () {
    this.getcateringItems()
  },
  methods: {
    getcateringItems() {
      axios({
        method: 'get',
        url: API_URL + 'catering/',
        auth: {
          username: 'freddy',
          password: 'voldermort'
        }
      }).then(response => this.cateringitems = response.data)
    },
    checkDatabase() {
      if (this.libraryitems == '' ) {
        this.message = 'You have been successfully cleared from this department';
        this.alert = 'alert alert-success'
      }
      else {
        this.message = 'Please check with the department and clear your record before proceeding.'
        this.showTable =  true;
        this.alert = 'alert alert-danger'
      }
    }
  }
}
</script>

<style scoped>

</style>
