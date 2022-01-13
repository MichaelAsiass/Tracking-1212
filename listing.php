?php    
    
include "connection.php";    
    
if(isset($_GET['id'])){    
$sql = "delete from registration where id = '".$_GET['id']."'";    
$result = mysql_query($sql);    
}    
    
$sql = "select * from registration";    
$result = mysql_query($sql);    
?>    
<html>    
    <body>    
        <table width = "100%" border = "1" cellspacing = "1" cellpadding = "1">    
            <tr>    
                <td>Id</td>    
                <td>Link/td>    
                <td>Price From</td>    
                <td>Price To</td>    
                <td>Email</td>    
            </tr>    
        </table>    
    </body>    
</html>    


<?php    
    
while($row = mysql_fetch_object($result)){    
    
    
?>  
    <tr>  
        <td>  
            <?php echo $row->id;?>  
        </td>  
        <td>  
            <?php echo $row->Link;?>  
        </td>  
        <td>  
            <?php echo $row->Price From;?>  
        </td>  
        <td>  
            <?php echo $row->Price To;?>  
        </td>  
        <td>  
            <?php echo $row->Email;?>  
        </td>  
        <td>  
            <?php echo $row->attach_file;?>  
        </td>  
        <td> <a href="listing.php?id =     
            <?php echo $row->id;?>" onclick="return confirm('Are You Sure')">Delete    
        </a> | <a href="index.php?id =     
            <?php echo $row->id;?>" onclick="return confirm('Are You Sure')">Edit    
        </a> </td>  
        <tr>  
            <? php } ?>  