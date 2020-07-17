<template>
  <div>
   <div id="nav">
     <Header/>
   </div>
    <router-view />
    <br>
    <div class="container">
      <h3 class="title">School Clearance Form</h3>

    <br>
      <br>
      <DeanSchool/>
      <br>
      <HoD/>
      <br>
      <DeanStudents/>
      <br>
      <Games/>
      <br>
      <Hostels/>
      <br>
      <Catering/>
      <br>
      <Labs/>
      <br>
      <Registrar/>
      <br>
      <FinanceOfficer/>
      <br>
      <Finance/>
      <br>
      <Library/>
      <br><br><br><br><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TokenService from './storage/service'
import DeanSchool from './views/DeanSchool'
import HoD from './views/HoD'
import DeanStudents from './views/DeanStudents'
import Games from './views/GamesDepartment'
import Hostels from './views/Hostels'
import Catering from './views/Catering'
import Labs from './views/LabsandWorkshops'
import Registrar from './views/RegistrarofAcademics'
import FinanceOfficer from './views/FinanceOfficer'
import Finance from './views/Finance'
import Library from './views/Library'
import Header from './components/Header'

export default {
  name: 'App',
  components: {
    DeanSchool,
    HoD,
    DeanStudents,
    Games,
    Hostels,
    Catering,
    Labs,
    Registrar,
    FinanceOfficer,
    Finance,
    Library,
    Header
  },
  data(){
    return {
      username: '',
      password: '',
      token: localStorage.getItem('user-token') || null,
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/auth/', {
        username: this.username,
        password: this.password,
      })
      .then(resp => {
        
      this.token = resp.data.token;
      console.log(this.token)
      localStorage.setItem('user-token', resp.data.token)
      })
      .catch(error => {
        localStorage.removeItem('user-token')
      })
    },
    logout() {
      localStorage.removeItem('user-token');
      this.token = null;
    },
    register() {
      console.log('Router')
    },

  },
  created() {
    this.token = TokenService.getToken() || null;
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
