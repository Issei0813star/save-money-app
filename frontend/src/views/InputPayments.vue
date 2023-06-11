<template>
  <div>
    <nav>
      <v-btn @click="switchPaymentType('spending')">支出</v-btn>
      <v-btn @click="switchPaymentType('income')">収入</v-btn>
    </nav>
    <input-template
      :payment-type="paymentType"
      ref="inputTemplate"
    ></input-template>
  </div>
</template>

<script>
import InputTemplate from '../components/InputTemplate.vue'
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
  },
}
</script>
