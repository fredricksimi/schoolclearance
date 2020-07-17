<template>
  <div class="container" style="background-color:rgb(247, 231, 231)">
    <br><br>
    <p class="text-muted">Labs and Workshops</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <div :class="alert">{{message}}</div>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="labitem.id" v-for="labitem in labsitems">
        <td>
          {{labitem.item_name}}
        </td>
        <td>
          {{labitem.cash_value}}
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
  name: 'LabsandWorkshops',
  data () {
    return {
      labsitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: '',
      alert:''
    }
  },
  methods: {
    getlabsItems() {
      axios({
        method: 'get',
        url: API_URL + 'labs/'
      }).then(response => this.labsitems = response.data)
    },
    checkDatabase() {
      if (this.labsitems == '' ) {
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
