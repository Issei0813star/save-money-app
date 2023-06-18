<template>
  <div>
    <nav>
      <v-btn @click="switchPaymentType('spending')">支出</v-btn>
      <v-btn @click="switchPaymentType('income')">収入</v-btn>
    </nav>
    <input-template
      :payment-type="paymentType"
      ref="inputTemplate"
      @register="register"
    ></input-template>
  </div>
</template>

<script>
import InputTemplate from '../components/InputTemplate.vue'
import ApiService from '@/apiService.js'
import { showToaster } from '@/showToaster.js'

export default {
  name: 'InputPayments',
  components: {
    InputTemplate,
  },
  data: function () {
    return {
      paymentType: 'spending',
    }
  },
  methods: {
    switchPaymentType(type) {
      this.paymentType = type
      this.$refs.inputTemplate.inputedData.category = undefined
    },
    async register(paymentData) {
      const sendData = { ...paymentData, type: this.paymentType }
      const api = new ApiService()
      const result = await api.postPaymentData(sendData)
      if (result) {
        showToaster('登録成功')
      } else {
        showToaster('登録失敗', 'danger')
      }
    },
  },
}
</script>
