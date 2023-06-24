<template>
  <div class="report">
    <h1>収支レポート</h1>
  </div>
</template>

<script>
import ApiService from '@/apiService.js'

export default {
  name: 'PaymentsReport',
  components: {},

  async beforeMount() {
    const api = new ApiService()
    const targetMonth = this.getCurrentMonth()
    await api.getMonthPayments(targetMonth)
  },

  methods: {
    getCurrentMonth() {
      const currentDate = new Date()
      const year = currentDate.getFullYear()
      const month = (currentDate.getMonth() + 1).toString().padStart(2, '0')
      const formattedDate = `${year}-${month}`
      return formattedDate
    },
  },
}
</script>
