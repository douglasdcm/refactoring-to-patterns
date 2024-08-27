from src.encapsulate_classes_with_factory import (
    run_refac,
    DefaultDescriptorRefac,
    ReferenceDescriptorRefac,
)


def test_refac():
    default, reference = run_refac()
    assert isinstance(default, DefaultDescriptorRefac)
    assert isinstance(reference, ReferenceDescriptorRefac)
