import axios from 'axios'

class ApiService {
  constructor() {
    this.api = axios.create({
      baseURL: 'http://127.0.0.1/api',
    })
  }

  async getMonthPayments(targetDate) {
    try {
      await this.api.get('/payments/month', {
        params: {
          targetDate,
        },
      })
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
