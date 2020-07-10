<template>
  <div class="container" style="background-color:rgb(240, 229, 255)">
    <br><br>
    <p class="text-muted">Dean of Students</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <div :class="alert">{{message}}</div>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="dsitem.id" v-for="dsitem in deanstudentsitems">
        <td>
          {{dsitem.item_name}}
        </td>
        <td>
          {{dsitem.cash_value}}  
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
  name: 'DeanStudents',
  data () {
    return {
      deanstudentsitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: '',
      alert:''
    }
  },
  mounted () {
    this.getDeanStudentsItems()
  },
  methods: {
    getDeanStudentsItems() {
      axios({
        method: 'get',
        url: API_URL + 'dean-of-students/',
        auth: {
          username: 'freddy',
          password: 'voldermort'
        }
      }).then(response => this.deanstudentsitems = response.data)
    },
    checkDatabase() {
      if (this.deanstudentsitems == '' ) {
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
