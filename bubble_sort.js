// bubble sort by javascript
var list =[3,7,4,6,4,9,8,23,11,33,21,13]
function bubbleSort(list){
    for(var i = 0 ; i < list.length; i++){
        for(var j = 0; j < list.length - i - 1 ;j++ ){
            if(list[j] > list[j+1]){
                T = list[j]
                list[j] = list[j+1]
                list[j+1] = T
            }
        }
    }
    return list
}
console.log(bubbleSort(list))
