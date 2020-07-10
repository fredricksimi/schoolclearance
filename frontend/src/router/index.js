import Vue from 'vue'
import VueRouter from 'vue-router'
// import DeanSchool from '../views/DeanSchool.vue'
// import Finance from '../views/Finance.vue'


Vue.use(VueRouter)

const routes = [
  // { path: '/', name: 'deanschool', component: DeanSchool, mode: history },
  // { path: '/hod', name: 'hod', component: () => import( '../views/HoD.vue')},
  // { path: '/finance', name: 'finance', component: Finance },
  // { path: '/labs', name: 'labs', component: () => import( '../views/LabsandWorkshops.vue')},
  // { path: '/catering', name: 'catering', component: () => import( '../views/Catering.vue')},
  // { path: '/games', name: 'games', component: () => import( '../views/GamesDepartment.vue')},
  // { path: '/hostels', name: 'hostels', component: () => import( '../views/Hostels.vue')},
  // { path: '/library', name: 'library', component: () => import( '../views/Library.vue')},
  // { path: '/registrar-of-academics', name: 'registrar-of-academics', component: () => import( '../views/RegistrarofAcademics.vue')},
  // { path: '/dean-of-students', name: 'dean-of-students', component: () => import( '../views/DeanStudents.vue')},
  // { path: '/finance-officer', name: 'finance-officer', component: () => import( '../views/FinanceOfficer.vue')},

]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
