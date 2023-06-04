<template>
  <div class="input-template">
    <div class="input-field">
      <div class="text-field">
        <v-text-field
          label="日付"
          placeholder="日付を入力"
          color="blue"
          clearable
        >
        </v-text-field>
        <v-text-field
          label="金額"
          placeholder="金額を入力"
          color="blue"
          clearable
        >
        </v-text-field>
      </div>
      <div class="category-field">
        <ul v-for="category in paymentTypeData.categories" :key="category">
          <li>{{ category }}</li>
        </ul>
      </div>
    </div>
    <v-btn variant="outlined"> {{ paymentTypeData.type }}を登録 </v-btn>
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
    }
  },
  computed: {
    paymentTypeData() {
      return this.paymentType === 'spending'
        ? { type: '支出', categories: this.spendingCategories }
        : { type: '収入', categories: this.incomeCategories }
    },
  },
}
</script>

<style>
ul {
  list-style: none;
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
}

.category-field {
  width: 300px;
}
</style>
