<template>
  <div class="container" style="background-color:#acdefa">
    <br><br>
    <p class="text-muted">Library</p>
    <p>I certify that my records for the Catering Department are clear</p>
    
    <button @click="checkDatabase" class="btn btn-primary btn-sm">Clear this department</button>
    <br><br>
    <div :class="alert">{{message}}</div>
    <br>
    <table v-if="showTable" class="table table-bordered">
      
      <th>Item Name</th>
      <th>Cash Value</th>

      <tr :key="libitem.id" v-for="libitem in libraryitems">
        <td>
          {{libitem.item_name}}
        </td>
        <td>
          {{libitem.cash_value}}
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
  name: 'Library',
  data () {
    return {
      libraryitems: [],
      item_name: '',
      cash_value: '',
      showTable:false,
      message: '',
      alert: ''
    }
  },
  mounted () {
    this.getlibraryItems()
  },
  methods: {
    getlibraryItems() {
      axios({
        method: 'get',
        url: API_URL + 'library/',
        auth: {
          username: 'freddy',
          password: 'voldermort'
        }
      }).then(response => this.libraryitems = response.data)
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
