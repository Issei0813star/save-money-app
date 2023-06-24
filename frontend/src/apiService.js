import axios from 'axios'

class ApiService {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://127.0.0.1:5000/api',
    })
  }

  async getMonthPayments(targetMonth) {
    try {
      const res = await this.api.get('/payments/month', {
        params: {
          targetMonth,
        },
      })
      return res.data
    } catch (error) {
      console.error(error)
    }
  }

  async postPaymentData(paymentData) {
    try {
      await this.api.post('/payment', paymentData)
      return true
    } catch (error) {
      console.error(error)
      return false
    }
  }
}

export default ApiService
