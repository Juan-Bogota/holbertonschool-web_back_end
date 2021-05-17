import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(amount) {
    if (typeof amount !== 'number') throw new Error('amount must be an number');
    this._amount = amount;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) throw new Error('currency must be an Currency Class');
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') throw new Error('amount must be an number');
    if (typeof conversionRate !== 'number') throw new Error('conversion Rate must be an number');
    return amount * conversionRate;
  }
}
