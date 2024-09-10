const sum = () => {
    let INDICE = 12
    let SOMA = 0
    let K = 1

    while (K < INDICE) {
        K += 1
        SOMA += K
    }
    return SOMA
}


console.log(sum()) 
// Output: 77