<template>
  <div class="container" style="background-color: rgb(195, 253, 255)">
    <br><br>
    <p class="text-muted">Registrar of Academics</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <div :class="alert">{{message}}</div>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="raitem.id" v-for="raitem in RegistrarofAcademicsitems">
        <td>
          {{raitem.item_name}}
        </td>
        <td>
          {{raitem.cash_value}}
        </td>
      </tr>
    </table>
    <br>
  </div>
</template>

<script>
import TokenService from '../storage/service'
import axios from 'axios'
export default {
  name: 'RegistrarofAcademics',
  data () {
    return {
      RegistrarofAcademicsitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: '',
      alert:''
    }
  },
  methods: {
    getRegistrarofAcademicsItems() {
      axios.get('http://127.0.0.1:8000/registrar/', {
      headers: {
        'Authorization': `token ${TokenService}`
      }
      }).then(response => this.RegistrarofAcademicsitems = response.data)
    },
    checkDatabase() {
      if (this.RegistrarofAcademicsitems == '' ) {
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
