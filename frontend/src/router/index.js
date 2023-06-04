import { createRouter, createWebHistory } from 'vue-router'
import PaymentsReport from '../views/PaymentsReport.vue'
import WrightPayments from '../views/WrightPayments.vue'

const routes = [
  {
    path: '/',
    name: 'payments-report',
    component: PaymentsReport,
  },
  {
    path: '/wright',
    component: WrightPayments,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
