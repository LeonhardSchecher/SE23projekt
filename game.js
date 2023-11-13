

// tühi mänguväli
const empty_array2D =  [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];

//Järgnev plokk kontrollib, kas keegi on võitnud.
function win_state_hor(array_2D, player) {
    let in_row = false;
    for (let row of array_2D) {
        in_row = true;
        for (let val of row) {
            if (val !== player) {
                in_row = false;
                break;
            }
        }
        if (in_row) {
            return true;
        }
    }
    return false;
}
//testimiseks vajalik
let test = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 0]
];

function transpo(array_2D) {
    let tr_array = [];

    for (let i = 0; i < array_2D[0].length; i++) {
        tr_array[i] = [];
        for (let j = 0; j < array_2D.length; j++) {
            tr_array[i][j] = array_2D[j][i];
        }
    }
    return tr_array;
}

function flip_rows(array_2D) {
    let flipped = [];
    for (let i = 0; i < array_2D.length; i++) {
        flipped[i] = array_2D[i].slice().reverse();
    }
    return flipped;
}

function win_state_lrc(array_2D, player) {
    let state = true;
    for (let i = 0; i < array_2D.length; i++) {
        if (array_2D[i][i] !== player) {
            state = false;
            break;
        }
    }
    return state;
}
// See kutsub välja kõik vajalikud funktsioonid. Peab pöörduma siia
function win_state(array_2D, player) {
    const fn_vals = [
        win_state_hor(array_2D, player),
        win_state_hor(transpo(array_2D), player),
        win_state_lrc(array_2D, player),
        win_state_lrc(flip_rows(array_2D), player)
    ];
    return fn_vals.includes(true);
}


