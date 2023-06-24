import { Notyf } from 'notyf'
import 'notyf/notyf.min.css'

const notyf = new Notyf()

export function showToaster(message, type = 'success') {
  notyf.open({
    type: type,
    message: message,
    ripple: false,
    duration: 3000,
    position: {
      x: 'center',
      y: 'bottom',
    },
  })
}
