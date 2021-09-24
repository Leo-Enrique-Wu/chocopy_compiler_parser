package chocopy.common.astnodes;

import java_cup.runtime.ComplexSymbolFactory.Location;

/**
 * Base of all AST nodes representing expressions.
 * <p>
 * There is nothing in this class, but there will be many AST
 * node types that have fields that are *any expression*. For those
 * cases, having a field of this type will encompass all types of
 * expressions such as binary expressions and literals that subclass
 * this class.
 */
public abstract class Expr extends Node {

    /**
     * A Python expression spanning source locations [LEFT..RIGHT].
     */
    public Expr(Location left, Location right) {
        super(left, right);
    }
}
