import 'package:expenses/models/transaction.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class Chart extends StatelessWidget{
  final List<Transaction> recentTransactions;
  const Chart(this.recentTransactions, {Key? key}) : super(key: key);

  List<Map<String, Object>> get groupTransactions{
    return List.generate(7, (index){
      final weekDay =  DateTime.now().subtract(
        Duration(days: index),
      );
      double totalSum = 0.0;
      for(var i = 0; i < recentTransactions.length; i++){
        bool sameDay = recentTransactions[i].date.day == weekDay.day;
        bool sameMonth = recentTransactions[i].date.month == weekDay.month;
        bool sameYear = recentTransactions[i].date.year == weekDay.year;
        if(sameDay && sameMonth && sameYear){
          totalSum += recentTransactions[i].value;
        }
      }
      return {
        'day': DateFormat.E().format(weekDay)[0],
        'value': totalSum,
      };
    }
    );
  }

  @override
  Widget build(BuildContext context){
    groupTransactions;
    return Card(
      elevation: 6,
      margin: const EdgeInsets.all(20),
      child: Row(
        children: groupTransactions.map((tr){
          return Text('${tr['day']}: ${tr['value']}');
        }).toList(),
      ),
    );
  }
}