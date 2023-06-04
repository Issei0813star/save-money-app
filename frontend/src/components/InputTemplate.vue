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
        <p>カテゴリー</p>
      </div>
    </div>
    <v-btn variant="outlined"> {{ paymentTypeData }}を登録 </v-btn>
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
  computed: {
    paymentTypeData() {
      return this.paymentType === 'spending' ? '支出' : '収入'
    },
  },
}
</script>

<style>
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
