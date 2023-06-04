<template>
  <div>
    <nav>
      <v-btn @click="paymentType = 'spending'">支出</v-btn>
      <v-btn @click="paymentType = 'income'">収入</v-btn>
    </nav>
    <input-template :payment-type="paymentType"></input-template>
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
}
</script>
