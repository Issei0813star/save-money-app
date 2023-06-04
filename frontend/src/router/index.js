import { createRouter, createWebHistory } from 'vue-router'
import PaymentsReport from '../views/PaymentsReport.vue'
import InputPayments from '../views/InputPayments.vue'

const routes = [
  {
    path: '/',
    name: 'payments-report',
    component: PaymentsReport,
  },
  {
    path: '/input',
    component: InputPayments,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
