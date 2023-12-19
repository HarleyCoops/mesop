from typing import Any, TypeVar, cast

from mesop.dataclass_utils import dataclass_with_defaults
from mesop.runtime import runtime

T = TypeVar("T")


def state(state: type[T]) -> T:
  return runtime().context().state(state)


def stateclass(cls: type[T] | None, **kw_args: Any) -> type[T]:
  """
  Similar as dataclass, but it also registers with Mesop runtime().
  """

  def wrapper(cls: type[T]) -> type[T]:
    dataclass_cls = dataclass_with_defaults(cls, **kw_args)
    runtime().register_state_class(dataclass_cls)
    return dataclass_cls

  if cls is None:
    # too difficult to properly type annotate
    anyWrapper = cast(Any, wrapper)
    # We're called with parens.
    return anyWrapper

  return wrapper(cls)
