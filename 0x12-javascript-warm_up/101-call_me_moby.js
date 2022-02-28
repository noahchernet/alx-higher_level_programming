#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  x = parseInt(x);
  if (!isNaN(x)) {
    while (x--) {
      theFunction();
    }
  }
};
