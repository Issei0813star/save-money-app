<template>
  <div class="input-template">
    <div class="input-field">
      <div class="left-field">
        <v-text-field
          label="日付"
          placeholder="日付を入力"
          color="blue"
          clearable
          type="date"
          v-model="inputedData.date"
          :rules="dateRule"
        ></v-text-field>
        <v-text-field
          label="金額"
          placeholder="金額を入力"
          color="blue"
          clearable
          type="number"
          v-model="inputedData.amount"
          :rules="amountRule"
        ></v-text-field>
      </div>
      <div class="right-field">
        <v-select
          :items="paymentTypeData.categories"
          label="カテゴリー"
          v-model="inputedData.category"
          :rules="categoryRule"
        ></v-select>

        <input type="checkbox" v-model="isCredit" />
        <label>クレジット払い</label>
      </div>
    </div>
    <v-btn
      variant="outlined"
      :disabled="!validateInputedData"
      @click="registerPayment"
    >
      {{ paymentTypeData.type }}を登録
    </v-btn>
  </div>
</template>

<script>
import { ref, reactive, computed } from 'vue'

export default {
  props: {
    paymentType: {
      type: String,
      required: true,
    },
  },
  setup(props, { emit }) {
    const spendingCategories = [
      '食費',
      '日用品',
      'ファッション',
      '交際費',
      'Vape',
      '光熱費',
      '住居費',
      '仕事道具',
      '交通費',
    ]
    const incomeCategories = ['給料', '臨時収入']

    const inputedData = reactive({
      amount: undefined,
      date: undefined,
      category: undefined,
    })

    const amountRule = [
      (value) =>
        (value && value.length !== 0 && value === inputedData.amount) ||
        '入力必須',
    ]
    const dateRule = [
      (value) =>
        (value && value.length !== 0 && value === inputedData.date) ||
        '入力必須',
    ]
    const categoryRule = [
      (value) =>
        (value && value.length !== 0 && value === inputedData.category) ||
        '入力必須',
    ]

    const isCredit = ref(false)

    const paymentTypeData = computed(() => {
      return props.paymentType === 'spending'
        ? { type: '支出', categories: spendingCategories }
        : { type: '収入', categories: incomeCategories }
    })

    const validateInputedData = computed(() => {
      return Object.values(inputedData).every((value) => value)
    })

    const registerPayment = () => {
      const paymentData = { ...inputedData, isCredit: isCredit.value }
      inputedData.amount = undefined
      inputedData.category = undefined
      inputedData.date = undefined
      isCredit.value = false
      emit('register', paymentData)
    }

    return {
      inputedData,
      amountRule,
      dateRule,
      categoryRule,
      isCredit,
      paymentTypeData,
      validateInputedData,
      registerPayment,
    }
  },
}
</script>

<style>
ul {
  list-style: none;
}

li:hover {
  color: rgb(35, 127, 232);
  cursor: pointer;
}

.input-template {
  margin-top: 50px;
}

.input-field {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.left-field {
  width: 300px;
  padding-right: 20px;
}

.right-field {
  width: 300px;
  padding-left: 20px;
}
</style>
