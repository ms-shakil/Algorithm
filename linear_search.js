// linear_search algorithm 
var list =[2,4,5,7,8,9,10,64]
var value =11
function linearSearch(list,value){
    for(var i= 0;i<list.length;i++){
        if(list[i]==value){
            return i
        }
    }
    return -1
}
console.log(linearSearch(list,value))