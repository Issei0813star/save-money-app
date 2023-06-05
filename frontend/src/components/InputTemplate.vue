<template>
  <div class="input-template">
    <div class="input-field">
      <div class="text-field">
        <v-text-field
          label="日付"
          placeholder="日付を入力"
          color="blue"
          clearable
          type="date"
          v-model="inputedData.date"
          :rules="dateRule"
        >
        </v-text-field>
        <v-text-field
          label="金額"
          placeholder="金額を入力"
          color="blue"
          clearable
          type="number"
          v-model="inputedData.amount"
          :rules="amountRule"
        >
        </v-text-field>
      </div>
      <div class="category-field">
        <v-select
          :items="paymentTypeData.categories"
          label="カテゴリー"
          v-model="inputedData.category"
          :rules="categoryRule"
        ></v-select>
      </div>
    </div>
    <v-btn variant="outlined" :disabled="!validateInuptedData">
      {{ paymentTypeData.type }}を登録
    </v-btn>
  </div>
</template>

<script>
export default {
  props: {
    paymentType: {
      type: String,
      required: true,
    },
  },
  data: function () {
    return {
      spendingCategories: [
        '食費',
        '日用品',
        'ファッション',
        '交際費',
        'Vape',
        '光熱費',
        '住居費',
        '仕事道具',
        '交通費',
      ],
      incomeCategories: ['給料', '臨時収入'],
      selectedCategory: '未選択',
      inputedData: {
        amount: undefined,
        date: undefined,
        category: undefined,
      },
      amountRule: [
        (value) =>
          (value && value.length !== 0 && value === this.inputedData.amount) ||
          '入力必須',
      ],
      dateRule: [
        (value) =>
          (value && value.length !== 0 && value === this.inputedData.date) ||
          '入力必須',
      ],
      categoryRule: [
        (value) =>
          (value &&
            value.length !== 0 &&
            value === this.inputedData.category) ||
          '入力必須',
      ],
    }
  },
  computed: {
    paymentTypeData() {
      return this.paymentType === 'spending'
        ? { type: '支出', categories: this.spendingCategories }
        : { type: '収入', categories: this.incomeCategories }
    },
    validateInuptedData: function () {
      return !Object.values(this.inputedData).includes(undefined)
    },
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

.text-field {
  width: 300px;
  padding-right: 20px;
}

.category-field {
  width: 300px;
  padding-left: 20px;
}
</style>
