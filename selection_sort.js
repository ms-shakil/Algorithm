// selection sort by js
var list =[3,7,4,6,4,9,8,23,11,33,21,13]
function selection_Sort(list){
    for(var i = 0; i< list.length;i++){
        var index = i
        for (var j= i+1; j< list.length;j++){
            if(list[j]<list[i]){
                index = j
            }
        }
        if(index != i){
            T = list[i]
            list[i]= list[index]
            list[index]=T
        }
    }
    return list
}
console.log(selection_Sort(list))