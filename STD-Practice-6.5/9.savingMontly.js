function savingMonthly(payments, livingCost) {
  if (Array.isArray(payments) && !Array.isArray(livingCost)) {
    let AllPaymentAfterTax = 0;

    payments.forEach((money) => {
      if (money >= 3000) {
        AllPaymentAfterTax += money - money * 0.2;
      } else {
        AllPaymentAfterTax += money;
      }
    });

    const leftover = AllPaymentAfterTax - livingCost;

    if (leftover >= 0) {
      return leftover;
    } else {
      return "earn more";
    }
  } else {
    return "invalid input";
  }
}

console.log(savingMonthly([1000, 2000, 3000], 5400));
console.log(savingMonthly([1000, 2000, 2500], 5000));
console.log(savingMonthly([900, 2700, 3400], 10000));

console.log(savingMonthly(100, [900, 2700, 3400]));
