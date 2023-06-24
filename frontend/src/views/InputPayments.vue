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
import { ref, onMounted } from 'vue'
import InputTemplate from '../components/InputTemplate.vue'
import ApiService from '@/apiService.js'
import { showToaster } from '@/showToaster.js'

export default {
  name: 'InputPayments',
  components: {
    InputTemplate,
  },
  setup() {
    //data
    const paymentType = ref('spending')

    //methods
    const switchPaymentType = (type) => {
      paymentType.value = type
      clearInputData()
    }

    const clearInputData = () => {
      const inputTemplateRef = ref(null)
      if (inputTemplateRef.value) {
        inputTemplateRef.value.clearInputData()
      }
    }

    const register = async (paymentData) => {
      const sendData = { ...paymentData, type: paymentType.value }
      const api = new ApiService()
      const result = await api.postPaymentData(sendData)
      if (result) {
        showToaster('登録成功')
      } else {
        showToaster('登録失敗', 'danger')
      }
    }

    onMounted(() => {
      clearInputData()
    })

    return {
      paymentType,
      switchPaymentType,
      register,
    }
  },
}
</script>
