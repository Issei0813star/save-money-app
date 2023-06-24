<template>
  <div class="report">
    <h1>収支レポート</h1>
  </div>
</template>

<script>
import { ref, onBeforeMount } from 'vue'
import ApiService from '@/apiService.js'

export default {
  name: 'PaymentsReport',

  setup() {
    const paymentData = ref([])

    onBeforeMount(async () => {
      const api = new ApiService()
      const targetMonth = getCurrentMonth()
      paymentData.value = await api.getMonthPayments(targetMonth)
    })

    function getCurrentMonth() {
      const currentDate = new Date()
      const year = currentDate.getFullYear()
      const month = (currentDate.getMonth() + 1).toString().padStart(2, '0')
      const formattedDate = `${year}-${month}`
      return formattedDate
    }

    return {
      paymentData,
    }
  },
}
</script>
