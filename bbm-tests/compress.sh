current_date=`date '+%Y-%m-%d'`
output_filename=$(echo $1)_$current_date.tar.bz2

if [ $# -eq 0 || $# -gt 1 ]
then
    echo ""
    echo "Please pass source dir"
    echo "usage: ./compress.sh <source dir>"
    echo ""
    echo "example"
    echo "./compress.sh /var/data"
elif [ $# -gt 0 ]
    if [ -f "$output_filename" ]
    then
        echo "$output_filename is already there"
        exit 1
    else
        tar -cjf $output_filename $1
        exit 0
    fi
fi
#################################

Let's look at a selection from the "Orders" table:
OrderID	CustomerID	OrderDate
10308	2	1996-09-18
10309	37	1996-09-19
10310	77	1996-09-20

Then, look at a selection from the "Customers" table:
CustomerID	CustomerName	ContactName	Country
1	Alfreds Futterkiste	Maria Anders	Germany
2	Ana Trujillo Emparedados y helados	Ana Trujillo	Mexico
3	Antonio Moreno Taquería


SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID=Customers.CustomerID;


OrderID	CustomerName	OrderDate
10308	Ana Trujillo Emparedados y helados	9/18/1996
10365	Antonio Moreno Taquería	11/27/1996
10383	Around the Horn	12/16/1996
10355	Around the Horn	11/15/1996
10278	Berglunds snabbköp	8/12/1996

