grammar NodeTemplate;

tree_node : NAME ( param (',' param )* )?;

param : variable | glist | constant; // list is a keyword in python hence use glist here to avoid conflict

variable : NAME (':' vartype)? ('/' net)? ;
vartype  : NET | ECU | AP ;

net : netConstant | netVariable ;

glist          : assigned_list | unassigned_list ;
unassigned_list: '[' (ecuVariable | ecuConstant) DCOLON (ecuVariable | ecuConstant) ']' ;
assigned_list  : '[' ecuVariable '|' listVariable ']' ;

netVariable : NAME (':' NET)? ;
ecuVariable : NAME (':' (ECU|AP))? ('/' net)? ;
listVariable : NAME ;

constant: '@'NAME ;
netConstant: '@'NAME ;
ecuConstant: '@'NAME ;

// first defined reserved keywords
AND : 'AND';
OR  : 'OR';
SAND: 'SAND';
NET : 'NET';
ECU : 'ECU';
AP  : 'AP' ;

// then defined the rest
NAME : [a-zA-Z][a-zA-Z0-9]*;

DCOLON: '..';
WS : [ \t\r\n]+ -> skip ;