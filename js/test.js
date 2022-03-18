let num = 512;
// let numIntoStr = num.toString();
let revStr = ""
let finalWord = ""

// for (let i = 0; i < numIntoStr.length; i++) {
//     returnStr = convertIntoWord(numIntoStr[i])
//     finalWord += returnStr
// }

while (num > 0) {
    let rem = num % 10
    revStr = convertIntoWord(rem)
    finalWord = revStr + " " + finalWord
    num = Math.floor(num / 10)
}

console.log(finalWord)

function convertIntoWord(str) {

    if (str === 1) {
        return "One"
    } else if (str === 2) {
        return "Two"
    }
    else if (str === 3) {
        return "Three"
    }
    else if (str === 4) {
        return "Four"
    } else if (str === 5) {
        return "Five"
    } else if (str === 6) {
        return "Six"
    } else if (str === 7) {
        return "Seven"
    } else if (str === 8) {
        return "Eight"
    } else if (str === 9) {
        return "Nine"
    } else {
        return "Zero"
    }
}

