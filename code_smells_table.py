# It matches the code smells (key) with the refactorings that fix it (value)
from src import (
    chain_constructors,
    form_template_method,
    introduce_polymorphic_creation_with_factory_method,
    replace_one__many_distinctions_with_composite,
    extract_composite,
    unify_interfaces_with_adapter,
    introduce_null_object,
    compose_method,
    replace_conditional_logic_with_strategy,
    replace_conditional_dispatcher_with_command,
    move_accumulation_to_collecting_parameter,
    move_accumulation_to_visitor,
    introduce_null_object,
    move_emblishment_to_decorator,
    replace_state_altering_conditionals_with_state,
    encapsulate_composite_with_builder,
    replace_implict_tree_with_composite,
    replace_implicit_language_with_interpreter,
    replace_type_code_with_class,
    encapsulate_classes_with_factory,
    move_creation_knowledge_to_factory,
    unify_interfaces_with_adapter,
    inline_singleton,
)


class CodeSmells:
    Duplicated_Code = [
        form_template_method,
        introduce_polymorphic_creation_with_factory_method,
        chain_constructors,
        replace_one__many_distinctions_with_composite,
        extract_composite,
        unify_interfaces_with_adapter,
        introduce_null_object,
    ]
    Long_Method = [
        compose_method,
        move_accumulation_to_collecting_parameter,
        replace_conditional_dispatcher_with_command,
        move_accumulation_to_visitor,
        replace_conditional_logic_with_strategy,
    ]
    Conditional_Complexity = [  # Complicated conditonal logic
        replace_conditional_logic_with_strategy,
        move_emblishment_to_decorator,
        replace_state_altering_conditionals_with_state,
        introduce_null_object,
    ]
    Primitive_Obssession = [
        replace_type_code_with_class,
        replace_state_altering_conditionals_with_state,
        replace_conditional_logic_with_strategy,
        replace_implict_tree_with_composite,
        replace_implicit_language_with_interpreter,
        move_emblishment_to_decorator,
        encapsulate_composite_with_builder,
    ]
    # Lack of "information hidin" [Parnas]
    Indecent_Exposure = [encapsulate_classes_with_factory]
    # The logic/responsibility is sprawled in multiple places (classes, methods)
    Solution_Sprawl = [move_creation_knowledge_to_factory]
    # [Fowler and Beck] Interfaces of classes different, but classes are similar
    Alternative_Classes_with_Different_Interfaces = unify_interfaces_with_adapter
    # [Fowler and Beck] A class the doesn't do enough to pay itself
    Lazy_Class = [inline_singleton]
    Large_Class = [
        replace_conditional_dispatcher_with_command,
        replace_state_altering_conditionals_with_state,
        replace_implict_tree_with_composite,
    ]
    Switch_Statements = [  # Complicated switches
        replace_conditional_dispatcher_with_command,
        move_accumulation_to_visitor,
    ]
    # Code that do the same with different types or quantity of data (similar to duplication)
    Combination_Explostion = [replace_implicit_language_with_interpreter]
    # The same problem being solved in many ways in the system (similar to duplication)
    Oddball_Solutions = [unify_interfaces_with_adapter]
