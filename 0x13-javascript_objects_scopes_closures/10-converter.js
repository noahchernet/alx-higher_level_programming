#!/usr/bin/node

// Returns a function that converts a number to base @base
exports.converter = function (base) {
  return function (number) {
    const newNumberInBase = [];
    while (number) {
      newNumberInBase.unshift(number % base);
      number = Math.floor(number / base);
    }

    let strOfNewNumber = '';
    newNumberInBase.forEach(function (item) { strOfNewNumber += item; });

    // If the base is 16 and the number is between 10 and 15, assign it to the respective base 16 letter
    strOfNewNumber = parseInt(strOfNewNumber);
    if (base === 16) {
      if (strOfNewNumber === 10) {
        strOfNewNumber = 'a';
      } else if (strOfNewNumber === 11) {
        strOfNewNumber = 'b';
      } else if (strOfNewNumber === 12) {
        strOfNewNumber = 'c';
      } else if (strOfNewNumber === 13) {
        strOfNewNumber = 'd';
      } else if (strOfNewNumber === 14) {
        strOfNewNumber = 'e';
      } else if (strOfNewNumber === 15) {
        strOfNewNumber = 'f';
      }
    }

    return strOfNewNumber;
  };
};
