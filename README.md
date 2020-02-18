# Chronos: A public  timestamping service for Zilliqa 

There are many cases where a blockchain transaction is not required to achieve the benefit of a public ledger. A well-known example being a timestamp or other time artifact that can serve as a proof of existance prior to a certain point in time. Many examples exist for Bitcoin and other public ledgers, including BTStamp, OpenTimestamps and The Ethereum Chronos project. Zilliqa offers several unique properties that make timestamping against its pool of hashpower particularly attractive.
In comparison with OpenTimeStamps, which forwards to Bitcoin, our service can offer timestamps with an interval of 30s (the current Zilliqa blockchain) and finality in at most 1 minute. Bitcoin's Nakamoto consensus and long unreliable blocktime mean that a timestamp client must wait hours to a full day before they can be confident a timestamp will be upgraded to a full proof. 

Beyond that, Bitcoin's facility for native smart contracts is limited, while Zilliqa is a smart contract platform. The potential benefit for having a real-world oracle that exposes trustworthy proofs of existance on-chain is hard to fully imagine, but it certainly makes a lot of sense for the Zilliqa network to host this service, reliably and free of up-front cost in order to provide a more robust option to innovators looking to distrupt established processes in legal practices and financial applications worldwide. In some countries it is already included in the law that Blockchain-backed timestamps can be considered notorized if they can be audited.

This service's design borrows some from the OpenTimestamps project, but due to the differences between Zilliqa and Bitcoin it must be adapted heavily to achieve most benefit. The .ots file format may one day be supported, but for now we will rely on JSON, as one of the primary goals of this project is proofs between machines and servers. 


## System

### RPC Service

### Smart Contracts

### Incomplete and Complete Proof Files

### Client-side digest generation, privacy features.

## Development
