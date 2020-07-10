<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" >Clearance Form</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">

      <!-- <li class="nav-item active"><a class="nav-link"><router-link to="/">Dean of School</router-link></a></li> -->

      <!-- <li class="nav-item"><a class="nav-link"><router-link to="/hod">Head of Dept</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/dean-of-students">Dean of Students</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/library">Library</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/games">Games</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/labs">Labs and Workshops</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/registrar-of-academics">Registrar of Academics</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/finance-officer">Finance Officer</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/finance">Finance</router-link></a></li>

      <li class="nav-item"><a class="nav-link"><router-link to="/catering">Catering</router-link></a></li> -->
    </ul>
  </div>
</nav>
    
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
    Library
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
</style>
